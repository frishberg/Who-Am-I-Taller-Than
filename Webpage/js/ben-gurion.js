/**
 * This method takes an inputted name (ex. aron frishberg) and outputs the name formatted for 
 * displaying by capitalizing the first letter of each word (ex. Aron Frishberg).
 * @param name the given name to be formatted
 * @returns the formatted name
 */
function formatName(name) {
    temp = ""
    temp += name[0].toUpperCase();
    for (var i = 1; i < name.length; i++) {
        if (name[i - 1] == " ") {
            temp += name[i].toUpperCase();
        } else {
            temp += name[i];
        }
    }
    return temp
}
/**
 * This method converts centimeters to feet and inches for displaying purposes.
 * @param heightInCm 
 */
function convertToFeet(heightInCm) {
    var feet = Math.floor(heightInCm / 30.48);
    var inches = Math.round((heightInCm % 30.48) / 2.54);
    if (inches==12) {
        feet++;
        inches=0;
    }
    return feet + "'" + inches + '"';
}

/**
 * This method creates a listing of a celebirty on the index page.
 * @param name inputted name of the celebrity
 * @param height inputted height of the celebrity
 * @param networth inputted networth of the celebrity
 * @param popularity inputted popularity of the celebrity
 * @param img_src inputted image source of an image of the celebrity
 */
function createListing(name, height, networth, popularity, img_src, n) {
    //creating listing div
    var listing = document.createElement("div");
    listing.className = "listing";

    //adding fade in image
    listing.style = "animation-delay:" + Math.sqrt((n+1)/2) + "s;"

    //creating image
    var img = document.createElement("img");
    img.src = img_src;
    listing.appendChild(img);

    //adding &nbsp;
    listing.appendChild(document.createTextNode("\u00A0"));

    //creating listing-text div
    var listing_text = document.createElement("div");
    listing_text.className = "listing-text";

    //adding name
    var name_node = document.createElement("h1");
    name_node.innerHTML = formatName(name);
    listing_text.appendChild(name_node);

    //adding height
    var height_node = document.createElement("p");
    height_node.innerHTML = "Height: " + convertToFeet(height);
    listing_text.appendChild(height_node);

    //adding networth
    var networth_node = document.createElement("p");
    networth_node.innerHTML = "Networth: $" + formatMoney(networth);
    listing_text.appendChild(networth_node);

    //adding popularity
    var popularity_node = document.createElement("p");
    popularity_node.innerHTML = "Popularity Rank: " + popularity;
    listing_text.appendChild(popularity_node);

    //adding listing-text to listing
    listing.appendChild(listing_text);

    //adding listing to body
    document.getElementById('skeleton').appendChild(listing);
}

/**
 * Firstly, it clears all of the display listings on the page using the clearDisplay method.
 * This method retrieves the data from the json file.  It then ranks all of the celebrities by wikipedia searches, and 
 * creates "popularity_rank" for each celebrity object.  It then narrows down all the data (data) to 
 * the celebrities that are shorter than the user (targetData) by using the selectData method.  It then sorts the data 
 * by the user's choice in the select box using the sort method.  It then creates listings for each celebrity
 * using the createListing method.
 */
function update() {
    clearDisplay()
    var data = fetch("data.json")
        .then(response => response.json())
        .then(data => data = createPopularityRanks(data))
        .then(data => targetData = selectData(data))
        .then(targetData => targetData = sort(targetData))
        .then(targetData=> {
            for (var i = 0; i < targetData.length; i++) {
                createListing(targetData[i].name, targetData[i].height, targetData[i].networth, targetData[i].popularity_rank, "images/" + targetData[i].name + ".jpg", i);
            }
        })
}
/**
 * This method takes all of the data and returns all of the listings that are shorter than or equal to the user
 * @param data 
 * @returns 
 */
function selectData(data) {
    var feet = Number(document.getElementById("foot-box").value);
    var inches = Number(document.getElementById("inch-box").value);
    var user_height = feet * 30.48 + inches * 2.54;

    var targetData = [];
    for (var i = 0; i < data.length; i++) {
        if (data[i].height <= user_height) {
            targetData.push(data[i]);
        }
    }
    return targetData;
}
/**
 * This method takes in data and sorts it by the user's choice in the select box.  It allows for the sorting of 
 * the data by height, networth, and popularity.
 * @param data the inputted data
 * @returns the sorted data
 */
function sort(data) {
    var sort_by = document.getElementById("sort-by").value;
    if (sort_by == "name") {
        data.sort((a, b) => (a.name > b.name) ? 1 : -1);
    } else if (sort_by == "height") {
        data.sort((a, b) => (a.height < b.height) ? 1 : -1);
    } else if (sort_by == "networth") {
        data.sort((a, b) => (a.networth < b.networth) ? 1 : -1);
    } else if (sort_by == "popularity") {
        data.sort((a, b) => (a.popularity < b.popularity) ? 1 : -1);
    }
    return data;
}
/**
 * This method clears all of the listings on the page.
 */
function clearDisplay() {
    var skeleton = document.getElementById("skeleton");
    while (skeleton.firstChild) {
        skeleton.removeChild(skeleton.lastChild);
    }
}
/**
 * This method sorts the given data by the popularity field of each listing (wikipedia searches)
 * @param data the inputted data
 * @returns the sorted data
 */
function sortByPopulairty(data) {
    data.sort((a, b) => (a.popularity < b.popularity) ? 1 : -1);
    return data;
}
/**
 * This method goes through all of the listings in the inputted data and creates a popularity_rank field for each listing
 * @param data the inputted data
 * @returns the data with the popularity_rank field
 */
function createPopularityRanks(data) {
    data = sortByPopulairty(data);
    for (var i = 0; i < data.length; i++) {
        data[i].popularity_rank = i + 1;
    }
    return data
}

/**
 * This starts up everything when the page loads.
 */
window.onload = update;

/**
 * This method formats money to a form that displays better. (Ex. 246000000000 -> 246B)
 * @param {*} dollars 
 * @returns 
 */
function formatMoney(dollars) {
    endings = ["K", "M", "B"]
    endingIndex = -1;
    while(dollars>=1000) {
        dollars/=1000;
        endingIndex++;
    }
    temp = dollars + endings[endingIndex];
    return temp
}