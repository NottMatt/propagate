// Find all the posts that are related to inputted text value
function searchPosts()
{
    var textvalue = document.getElementById("searchbar").value;

    fetch("search?" + new URLSearchParams({"q": textvalue}))
        .then((response) => response.json())
        .then((data) =>
        {
            data.foreach(
                document.getElementById("feedBody").innerHTML += "<div class=\"feed-post\"><h2>Testing name</h2><h3>Testing desc</h3></div>"
            )
        });
}
