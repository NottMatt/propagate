// Find all the posts that are related to inputted text value
function searchPosts()
{
    console.log("Is happening.")
    var textvalue = document.getElementsByClassName("search-input").textvalue;

    fetch("search" + new URLSearchParams({"q": textvalue}))
        .then((response) => response.json())
        .then((data) => console.log(data));
}