// form.js
const form = document.getElementById('userForm');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    
    const formData = new FormData(form);
    const data = {
        name: formData.get('name'),
        contact: formData.get('contact'),
        details: formData.get('details')
    };

    fetch('https://yourdomain.com/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.text())
    .then(data => {
        alert(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
