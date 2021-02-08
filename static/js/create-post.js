const createPost = (ev) => {
    const data = {
        title: document.querySelector('#title').value,
        content: document.querySelector('#content').value,
        author: document.querySelector('#author').value
    };
    console.log(data);
    fetch('/api/posts', { 
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(showConfirmation);
    
    // this line overrides the default form functionality:
    ev.preventDefault();
};

const showConfirmation = (data) => {
    console.log('response from the server:', data);
    if (data.message && data.id) {
        document.querySelector('#post-form').classList.toggle("hide");
        document.querySelector('#confirmation').classList.toggle("hide");
    }
};

document.querySelector('#save').onclick = createPost;