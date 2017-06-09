#!/usr/bin/perl

use File::Basename;

die "Usage: $0 <lede images csv file> <path to content/>\n" if($#ARGV != 1);

my $csv = shift;
my $content = shift;


# read in the list of lede images
my %ledes;
open my $IN, "<$csv" or die "Can't open $csv: $!";

while(<$IN>)
{
  chomp;
  my @tokens = split(/;/);
  $ledes{$tokens[0]} = $tokens[1];
}

close $IN;


# find all .md files in content/
my @dirs = ($content);
my @mdfiles;

foreach my $dir (@dirs)
{
  opendir(my $dh, $dir) or die "Can't open $dir: $!";

  my @entries = readdir $dh;

  # remove hidden directories (including . and ..)
  @entries = grep { !/^\./ } @entries;

  # prepend the parent directory so we can actually access the content
  @entries = map { "$dir/$_" } @entries;

  # directories
  my @subdirs = grep { -d $_ } @entries;

  # .md files
  my @md = grep { -f $_ and /\.md$/ } @entries;

  push @dirs, @subdirs;
  push @mdfiles, @md;

  closedir $dh;
}


# go through all .md files, look for wordpress_id: in header and add the matching lede: line
foreach my $file (@mdfiles)
{
  open my $IN, "<$file" or die "Can't open $file: $!";
  my @lines = readline $IN;
  close $IN;

  open my $OUT, ">$file" or die "Can't open $file: $!";
  my $header = 1;
  foreach (@lines)
  {
    chomp;
    if($header)
    {
      # TODO
      if(/^wordpress_id:[ ]*([0-9]*)/)
      {
        my $lede = $ledes{$1};
        print basename($file, '.md');
        print "\n";
        print "$file\n";
        print "$lede\n\n";
        #print $OUT "wordpress_lede: $lede\n" if($lede);
      }
      elsif($_ eq "")
      {
        $header = 0;
      }
    }
    print $OUT "$_\n";
  }
  close $OUT;
}
