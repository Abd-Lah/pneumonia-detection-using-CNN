document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData();
    var fileInput = document.getElementById('file-input');
    formData.append('file', fileInput.files[0]);

    var loadingIcon = document.getElementById('loading-icon');
    var resultDiv = document.getElementById('result');
    
    loadingIcon.style.display = 'block'; // Display loading icon

    fetch('/predict', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
      .then(data => {
          loadingIcon.style.display = 'none'; // Hide loading icon
          
          if (data.error) {
              resultDiv.innerHTML = `<p id="error">${data.error}</p>`;
          } else {
              resultDiv.innerHTML = `<p>Prediction: ${data.label}</p>`;
          }
      }).catch(error => {
          console.error('Error:', error);
          loadingIcon.style.display = 'none'; // Hide loading icon
          resultDiv.innerHTML = `<p id="error">Error: ${error.message}</p>`;
      });
});

function predictImage(filename, folder) {
    var formData = new FormData();
    formData.append('filename', filename);
    formData.append('folder', folder);

    var loadingIcon = document.getElementById('loading-icon');
    var resultDiv = document.getElementById('result');
    
    loadingIcon.style.display = 'block'; // Display loading icon

    fetch('/predict', {
        method: 'POST',
        body: formData
    }).then(response => response.json())
      .then(data => {
          loadingIcon.style.display = 'none'; // Hide loading icon
          
          if (data.error) {
              resultDiv.innerHTML = `<p id="error">${data.error}</p>`;
          } else {
              resultDiv.innerHTML = `<p>Prediction: ${data.label}</p>`;
          }
      }).catch(error => {
          console.error('Error:', error);
          loadingIcon.style.display = 'none'; // Hide loading icon
          resultDiv.innerHTML = `<p id="error">Error: ${error.message}</p>`;
      });
}
