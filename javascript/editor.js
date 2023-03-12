// Retrieves the value of the parameter, if it exists.
function getUrlParam(name) {
    var results = new RegExp('[\\?&]' + name + '=([^&#]*)').exec(window.location.href);
    return (results && results[1]) || undefined;
}

// Attempts to load the file connected to the given id parameter.
function loadSavedFile() {
    try {
        id = getUrlParam("id")
        console.log(id)

        // With the id, we need to check to see if is in the database.
        fetch("component?", + new URLSearchParams({"id": id}))
        .then((response) => response.json())
        .then((data) =>
        {
            console.log(data)
        });
    }
    catch (error) {
        console.error(error)
    }
}