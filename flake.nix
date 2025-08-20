{
	description = "flake for python3";

	inputs = {
		nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
	};

	outputs = { self, nixpkgs, ...}: let
		pkgs = nixpkgs.legacyPackages."x86_64-linux";
	in {
		devShells.x86_64-linux.default = pkgs.mkShell {
		
			packages = with pkgs; [
				python3
				pyright
			];
		
		
			env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
				pkgs.stdenv.cc.cc.lib
				pkgs.libz
			];
		};
	};
}

