FROM mcr.microsoft.com/dotnet/aspnet:5.0
EXPOSE 80
WORKDIR /App
COPY bin/Release/net5.0 /App
ENTRYPOINT ["dotnet", "TodoApi.dll"]
