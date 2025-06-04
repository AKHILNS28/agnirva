const postForm = document.getElementById('postForm');
const postsContainer = document.getElementById('posts');
const apiUrl = 'http://localhost:5000/posts';
postForm.addEventListener('submit', async function(event) 
{
  event.preventDefault();
  const title = document.getElementById('title').value.trim();
  const content = document.getElementById('content').value.trim();
  if (!title || !content) {
    alert('Please fill in both fields');
    return;
  }
  try {
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content })
    });
    if (response.ok) {
      document.getElementById('title').value = '';
      document.getElementById('content').value = '';
      loadPosts(); // Refresh list
    } else {
      alert('Failed to create post');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Server error');
  }
});
async function loadPosts() {
  try {
    const response = await fetch(apiUrl);
    const posts = await response.json();
    displayPosts(posts);
  } catch (error) {
    console.error('Error loading posts:', error);
    alert('Could not load posts');
  }
}
function displayPosts(posts) {
  postsContainer.innerHTML = '';
  posts.forEach(post => {
    const postElement = document.createElement('div');
    postElement.className = 'post';
    postElement.innerHTML = `
      <h3>${post.title}</h3>
      <p>${post.content}</p>
      <button onclick="deletePost(${post.id})">Delete</button>
    `;
    postsContainer.appendChild(postElement);
  });
}
async function deletePost(id) 
{
  try 
  {
    const response = await fetch(`${apiUrl}/${id}`, {
      method: 'DELETE'
    });
    if (response.ok) {
      loadPosts();
    } else {
      alert('Failed to delete post');
    }
  } catch (error) {
    console.error('Error deleting post:', error);
    alert('Server error');
  }
}
loadPosts();