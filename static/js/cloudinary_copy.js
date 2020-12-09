
var myWidget = cloudinary.createUploadWidget({
  cloudName: "rmc-ltd",
  uploadPreset: 'my_garden',
    sources: [
        "local",
        "url",
        "camera",
        "image_search",
        "google_drive",
        "facebook",
        "dropbox",
        "instagram",
        "shutterstock"
    ],
    googleApiKey: "<image_search_google_api_key>",
    showAdvancedOptions: true,
    cropping: true,
    multiple: false,
    defaultSource: "local",
    styles: {
        palette: {
            window: "#464040",
            sourceBg: "#292222",
            windowBorder: "#c7a49f",
            tabIcon: "#cc6600",
            inactiveTabIcon: "#E8D5BB",
            menuIcons: "#ebe5db",
            link: "#ffb107",
            action: "#ffcc00",
            inProgress: "#99cccc",
            complete: "#78b3b4",
            error: "#ff6666",
            textDark: "#4C2F1A",
            textLight: "#D8CFCF"
        },
        fonts: {
            default: null,
            "'Merriweather', serif": {
                url: "https://fonts.googleapis.com/css?family=Merriweather",
                active: true
            }
        }
    }
    }, (error, result) => { 
    if (!error && result && result.event === "success") { 
      console.log('Done! Here is the image info: ', result.info); 
    }
  }
)

document.getElementById("upload_widget").addEventListener("click", function(){
    myWidget.open();
  }, false);