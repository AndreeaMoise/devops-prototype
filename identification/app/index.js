let base64 = ''

const getBase64String = (dataUrl) => dataUrl.split(',')[1];

document.addEventListener('DOMContentLoaded', () => {
	const form = document.querySelector('#verify-image');
	
	const file = document.querySelector("[name=image]");
	
	file.addEventListener("change", (event) => {
		const selectedfile = event.target.files;
		if (selectedfile.length > 0) {
			const [ imageFile ] = selectedfile;
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
		console.log(base64);
	});
})


