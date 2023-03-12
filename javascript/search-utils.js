// Find all the posts that are related to inputted text value
function searchPosts()
{
    var textvalue = document.getElementById("searchbar").value;

    fetch("search?" + new URLSearchParams({"q": textvalue}))
        .then((response) => response.json())
        .then((data) =>
        {
            var feedbody = document.getElementById("feed-body")
            feedbody.innerHTML = ""
            if (data.length == 0) {
                feedbody.innerHTML = "<p style=\"color: red\">No results</p>"
            }
            else {
                data.forEach(
                    element => feedbody.innerHTML +=
                    ("<div class=\"feed-post\" onclick=\"window.location.replace('gate-editor?id="
                    + element["component_id"]
                    + "')\"><h2>"
                    + element["component_name"]
                    + "</h2><h3>"
                    + element["description"]
                    + "</h3></div>")
                )
            }

        });
}

document.getElementById("searchbar").addEventListener("keyup", ({key}) => {
    if (key === "Enter") {
			searchPosts()
    }
})
