{ pkgs ? import <nixos-unstable> {}, ... }:

with rec {
  async_web_scrapper = pkgs.fetchFromGitHub {
    owner = "run4w4y";
    repo = "async_web_scrapper";
    rev = "516669989502ccc80a54910162a9854dbf09829e";
    sha256 = "1b4qvc5zwimcfpkhsb20z0lalgrvjsaq283mc8r8kiz2baz7lwgf";
  };
};
[
  (pkgs.python38.withPackages (p: with p; [
    trio sqlalchemy dateparser beautifulsoup4
  ]))
  (import "${async_web_scrapper}/default.nix")
]
