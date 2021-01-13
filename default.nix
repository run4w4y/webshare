with import <nixos-unstable> {};
with pkgs.python3Packages;

buildPythonPackage rec {
  name = "etsy_scrappers";
  src = ./.;
  propagatedBuildInputs = [];
  catchConflicts = false;
}