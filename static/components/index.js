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
		},
		handleUpdate() {
			const md = { id: '5b38eaf6-f978-11e9-bdf6-784f437c9885', category: 8 }
			console.info(md)
			axios.post('/update', md).then(res => {
				console.info(res)
			}).catch(res => {
				console.error('save error: ' + res);
				this.loading = false;
			});
		}
	}
});
