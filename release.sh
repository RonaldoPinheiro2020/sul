#!/bin/bash
# Pega a versão atual do arquivo VERSION
VERSION=$(cat VERSION)

echo "Lançando versão v$VERSION..."

git add .
git commit -m "chore: bump version to $VERSION"
git push origin main
git tag "v$VERSION"
git push origin "v$VERSION"

echo "Sucesso! O GitHub Actions agora vai gerar o Release v$VERSION automaticamente."