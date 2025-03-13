const showGithubList = () => {
    let githubList = document.getElementById("github-list");

    if (githubList.style.visibility === "hidden") {
        githubList.style.visibility = "visible";
        githubList.style.opacity = "1";

        setTimeout(() => {
            githubList.style.visibility = "hidden";
            githubList.style.opacity = "0"
        }, 5000)
    }

    else {
        githubList.style.visibility = "hidden";
        githubList.style.opacity = "0";
    }
};
