document.addEventListener('DOMContentLoaded', (ev)=>{
            let form = document.getElementById('myform');
            //get the captured media file
            let input = document.getElementById('image');
            
            input.addEventListener('change', (ev)=>{
                console.dir( input.files[0] );
                {
                    let img = document.getElementById('img');
                    img.src = URL.createObjectURL(input.files[0]);
                }
                
            })
            
        })