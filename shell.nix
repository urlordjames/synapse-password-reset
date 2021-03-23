{ pkgs ? import <nixpkgs> {} }:
let dependancies = python-packages: with python-packages; [
	requests
];
in pkgs.mkShell {
	buildInputs = with pkgs; [
		(python3.withPackages dependancies)
	];
}
