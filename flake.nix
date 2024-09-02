{
  description = "An environment for the Hugo static site generator ";

  inputs = {
    nixpkgs = {
      url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    };
  };

  outputs = { self, nixpkgs, ... }:
    let
      system = "x86_64-linux";
    in
    {
      devShells."${system}".default =
        let
          pkgs = import nixpkgs {
            inherit system;
          };
        in
        pkgs.mkShell {
          packages = with pkgs; [
            hugo
            yarn
            lychee
          ];
          shellHook = ''
            PROJECTDIR=`pwd`
            hugo-deploy() {
              echo "This doesn't do anything, but maybe it will one day."
            }
            hugo-server() {
               hugo server --disableFastRender -verbose
            }
            check-links() {
              cd $PROJECTDIR/content && lychee . && cd $PROJECTDIR
            }

            # hugo-server
          '';
        };
    };
}
