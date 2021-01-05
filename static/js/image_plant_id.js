document.querySelector('button').onclick = function sendIdentification() {
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
    //  console.log(base64files)
            
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
        
        // POST
        fetch('/hello', {

            // Declare what type of data we're sending
            headers: {
            'Content-Type': 'application/json'
            },

            // Specify the method
            method: 'POST',

            // A JSON payload
            body: JSON.stringify(data)

        }).then(function (response) { // At this point, Flask has printed our JSON
            return response.text();
        }).then(function (text) {

            console.log('POST response: ');

            // Should be 'OK' if everything was successful
            console.log(text);
            });

        console.log(data);

        })
    
      .catch((error) => {
        console.error('Error:', error);
      });
    })
};

