const b = document.querySelector('button');
const img = document.querySelector('#img');
const input = document.querySelector('input');

b.addEventListener('click', () => {
  const url = `https://yourdomain.com/form.html?ref=${encodeURIComponent(input.value)}`;
  console.log('Fetching URL:', url);
  
  fetch(`https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${url}`)
    .then(response => response.blob())
    .then(blob => {
      const objectURL = URL.createObjectURL(blob);
      img.src = objectURL;
      img.style.display = 'block';  // Show the image
    })
    .catch(error => console.error('Error:', error));
});
