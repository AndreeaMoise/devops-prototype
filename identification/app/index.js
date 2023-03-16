const truckId = '213456789';
const load = [
	{
		"sku": "124AB",
		"quantity": 28
	},
	{
		"sku": "1276AB",
		"quantity": 2
	},
	{
		"sku": "123ACB",
		"quantity": 10
	},
	{
		"sku": "124ABDEF",
		"quantity": 100
	},
	{
		"sku": "NM124AB",
		"quantity": 70
	}
];
let driverLocation = {
	latitude: null,
	longitude: null
};
let base64 = '';
let driverId = '';

document.addEventListener('DOMContentLoaded', () => {
	const form = document.querySelector('#verify-image');
	const file = document.querySelector("[name=image]");

	file.addEventListener("change", (event) => {
		const selectedfile = event.target.files;
		if (selectedfile.length > 0) {
			const [imageFile] = selectedfile;
			const fileReader = new FileReader();
			fileReader.onload = () => {
				const srcData = fileReader.result;
				base64 = getBase64String(srcData);
			};
			fileReader.readAsDataURL(imageFile);
		}
	});

	form.addEventListener("submit", async (event) => {
		event.preventDefault();
		login(base64, loggedIn);
	});

	document.querySelector("#sendTrace").addEventListener("click", sendTrace);
})

const getLocation = () => {
	if (navigator.geolocation) {
		console.log("Getting location..");
		navigator.geolocation.getCurrentPosition(onGetLocationSuccess);
	} else {
		console.log("Geolocation is not supported by this browser.");
	}
}

const onGetLocationSuccess = (position) => {
	driverLocation = {
		latitude: position.coords.latitude,
		longitude: position.coords.longitude
	};
	showPosition();
}

const showPosition = () => {
	hide("location");	
	setTimeout(() => {
		changeInnerHtml("locationLat", driverLocation.latitude);
		changeInnerHtml("locationLon", driverLocation.longitude);
		show("location");
	}, 500);
}

const login = (image, callback) => {
	axios.post(`${apiUrl}/verifyUser`, {
		image: image
	}).then(response => {
		driverId = JSON.parse(response.data.id);
		callback();
	}).catch(error => console.error(error));
};

const sendTrace = () => {
	const payload = {
		"driverId": driverId,
		"truckId": truckId,
		"location": driverLocation,
		"load": load
	};

	axios.post(`${apiUrl}/identification`, payload).then(response => {
		console.log(response);
	}).catch(error => console.error(error));
}

const loggedIn = () => {
	show('identification');
	changeInnerHtml('truckId', truckId);
	populateLoad();
	getLocation();
	setInterval(getLocation, 5000);
}

const populateLoad = () => {
	const table = document.getElementById("tableLoadBody");

	load.forEach(item => {
		const row = table.insertRow();
		const sku = row.insertCell(0);
		sku.innerHTML = item.sku;
		const quantity = row.insertCell(1);
		quantity.innerHTML = item.quantity;
	});
}

const getBase64String = (dataUrl) => dataUrl.split(',')[1];
const changeInnerHtml = (id, text) => document.getElementById(id).innerHTML = text;
const show = (id) => document.getElementById(id).style.display = "block";
const hide = (id) => document.getElementById(id).style.display = "none";