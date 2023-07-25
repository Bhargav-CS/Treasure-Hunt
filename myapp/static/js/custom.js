// Initialize Firebase SDK (use your Firebase configuration)
firebase.initializeApp(firebaseConfig);

// Reference to Firebase database
var database = firebase.database();
var postsRef = database.ref('/posts');

// Function to display posts
function displayPosts(data) {
    var postList = document.getElementById('postList');
    postList.innerHTML = '';

    data.forEach(function(postSnapshot) {
        var postData = postSnapshot.val();
        var li = document.createElement('li');
        li.innerHTML = '<strong>' + postData.title + '</strong><br>' + postData.content + '<br>Created at: ' + postData.created_at;
        postList.appendChild(li);
    });
}

// Listen for changes in Firebase data and update the HTML accordingly
postsRef.on('value', function(snapshot) {
    var postsData = [];
    snapshot.forEach(function(childSnapshot) {
        postsData.push(childSnapshot);
    });
    displayPosts(postsData);
});
