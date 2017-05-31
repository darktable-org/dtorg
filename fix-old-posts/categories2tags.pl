#!/usr/bin/perl

die "Usage: $0 <input .md file> [<output .md file>]\n" if($#ARGV != 0 && $#ARGV != 1);

open $IN, "<$ARGV[0]";

if($#ARGV == 1)
{
  open $OUT, ">$ARGV[1]";
  select $OUT;
}

$state = "HEADER"; # may be HEADER, PROCESS or POST
@tags;

# simple state machine:
#  - everything until a blank line is the header
#  - in the header there may be a "categories:" line -> process block
#  - in the header there may be a "tags:" line -> process block
#  - those two blocks need to be read and the content put into @tags
#  - once the header is done we print "tags:" and all values from @tags
#  - the rest of the file is printed verbatim.

while(<$IN>)
{
  my $print = 1;
  my $len = length($_);

  chomp;

  if($state eq "HEADER")
  {
    if($_ eq "")
    {
      $state = "POST";

      # print new "tags:"
      my $n_values = @tags;
      if($n_values > 0)
      {
        # TODO: do we want those in a single line, comma separated (tags: foo, bar, baz)
        #       or as a list as in the original file?
        my $tags_as_list = 0;
        if($tags_as_list)
        {
          print "tags:\n";
          foreach my $tag (@tags)
          {
            print "- $tag\n";
          }
        }
        else
        {
          print "tags: " . join(', ', @tags) . "\n";
        }
      }
    }
    elsif($_ eq "---")
    {
      $print = 0;
    }
    elsif($_ eq "categories:" || $_ eq "tags:")
    {
      $print = 0;
      $state = "PROCESS";
    }
  }
  elsif($state eq "PROCESS")
  {
    if($_ =~ /^[ ]*\-[ ]+([^ ]*)/)
    {
      $print = 0;
      push @tags, $1 if($1 ne "");
    }
    else
    {
      $print = 0;
      $state = "HEADER";
      # unread what we just looked at so that other code can act on it
      seek($IN, -$len, 1);
    }
  }

  print "$_\n" if($print);

}

close $IN;
close $OUT if($#ARGV == 1);
