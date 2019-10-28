new Vue({
	el: '#app-container',
	data() {
		return {
			
		};
	},
	methods: {
		handleSuccess(res, file, fileList) {
			console.log(res);
			console.log(typeof res);
			// console.log(file, fileList);
		}
	}
});
