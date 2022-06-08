FROM mcr.microsoft.com/dotnet/aspnet:5.0
EXPOSE 80
WORKDIR /App
COPY out/ /App
ENTRYPOINT ["dotnet", "TodoApi.dll"]