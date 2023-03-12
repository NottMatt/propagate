// Find all the posts that are related to inputted text value
function searchPosts()
{
    var textvalue = document.getElementById("searchbar").value;

    fetch("search?" + new URLSearchParams({"q": textvalue}))
        .then((response) => response.json())
        .then((data) => console.log(data));
}