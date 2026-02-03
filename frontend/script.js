const API_URL = 'http://127.0.0.1:5000/api/v1/books';

// 1. GET ALL BOOKS
async function fetchBooks() {
const response = await fetch(API_URL);
const data = await response.json();

const list = document.getElementById('bookList');
list.innerHTML = ''; // Clear current list

data.forEach(book => {
const li = document.createElement('li');
li.innerHTML = `
<span><strong>${book.title}</strong> by ${book.author}</span>
<button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>
`;
list.appendChild(li);
});
}

// 2. POST A NEW BOOK
async function addBook() {
const id = document.getElementById('bookId').value;
const title = document.getElementById('bookTitle').value;
const author = document.getElementById('bookAuthor').value;

await fetch(API_URL, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ id: parseInt(id), title, author })
});

fetchBooks(); // Refresh the list
}

// 3. DELETE A BOOK
async function deleteBook(id) {
await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
fetchBooks(); // Refresh the list
}
// Initial load
fetchBooks();