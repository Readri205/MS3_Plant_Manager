document.querySelector('submit').onclick = function sendIdentification() {
    const files = [...document.querySelector('input[type=file]').files];
    const promises = files.map((file) => {
      return new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onload = (event) => {
            const res = event.target.result;
        //    console.log(res);
            resolve(res);
          }
          reader.readAsDataURL(file)
      })
    })
    
    Promise.all(promises).then((base64files) => {
      console.log(base64files)
            
      const data = {
        api_key: "MgTIdDPkZpcC3NyLcl0wUfNYp6n24cRoKbc6MeyAIAqs4qW7EQ",
        images: base64files,
        modifiers: ["similar_images"],
        plant_details: ["common_names",
                          "url",
                          "wiki_description",
                          "taxonomy"]
      };
      
      fetch('https://api.plant.id/v2/identify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
    //    console.log('Success:', data);
        console.log(data);
      })
      .catch((error) => {
     //   console.error('Error:', error);
      });
    })
  
};