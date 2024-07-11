const b = document.querySelector('button');
const img = document.querySelector('#img');
const input = document.querySelector('input');

b.addEventListener('click', () => {
  const url = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${input.value}`;
  console.log('Fetching URL:', url);
  
  fetch(url)
    .then(response => {
      console.log('Response received');
      return response.blob();
    })
    .then(blob => {
      console.log('Blob created');
      const objectURL = URL.createObjectURL(blob);
      img.src = objectURL;
      img.style.display = 'block';  // Show the image
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
