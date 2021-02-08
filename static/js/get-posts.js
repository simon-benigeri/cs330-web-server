const getPosts = () => {
    fetch('/api/posts')
        .then(response => response.json())
        .then(displayPosts);
};

const toHTMLElement = (post) => {
    // formatting the date:
    const options = { 
        weekday: 'long', year: 'numeric', 
        month: 'long', day: 'numeric' 
    };
    const dateFormatted = new Date(post.published).toLocaleDateString('en-US', options);
    const snippetLength = 100;
    const snippet = post.content.length > snippetLength ? post.content.substring(0, snippetLength) + '...' : post.content;
    
    return `
        <section class="post">
            <a class="detail-link" href="/post/#${post.id}">
                <h2>${post.title}</h2>
            </a>
            <div class="date">${dateFormatted}</div>
            <p>${snippet}</p>
            <p>
                <strong>Author: </strong>${post.author}
            </p>
        </section>
    `;
};

const displayPosts = (data) => {
    const entries = [];
    for (const post of data) {
        entries.push(toHTMLElement(post));
    }
    document.querySelector('#posts').innerHTML = entries.join('\n');
};

getPosts();