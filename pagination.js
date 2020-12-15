baseUrl = "https://api.worldbank.org/v2/country/" + regionCode + "/indicator/SP.POP.TOTL?format=json"

//World Bank API for Pop Size
const baseUrlworldpop = "https://trefle.io/api/v1/species?token=TloaPWyjeiPTnJ20gEMLdZWpD0VoK1zunB_ooWNIjxA";
//GETs World Bank Population data by World from API
function getDataPop(cb) {
	const xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function () {
		if (this.readyState == 4 && this.status == 200) {
			cb(JSON.parse(this.responseText));
		}
	};
	xhttp.open("GET", baseUrlworldpop, true);
	xhttp.send();
	xhttp.onerror = function() {
		alert("Oops, the WB Country Population API return failed - please try again later, but please head over to the contact page and drop us an email so we can look at the error");
      };
      data = cb(JSON.parse(this.responseText))
      console.log(data)
}
getDataPop();