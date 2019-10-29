new Vue({
	el: '#app-container',
	data() {
		const cols = 4;
		return {
			metadatas: [],
			grids: {
				rows: 0, 
				cols,
				span: 24 /cols
			},
			categorys: [],
			tagTypes: ['success', 'warning', 'danger']
		};
	},
	watch: {
		metadatas() {
			this.grids.rows = Math.ceil(this.metadatas.length / this.grids.cols);
		}
	},
	created() {
		// const filepath = 'static/repos/H/Hs/20191029085119526723_cg_00022.jpg'
		// this.metadatas.push({ filepath })
		// this.metadatas.push({ filepath })
		// this.metadatas.push({ filepath: 'static/repos/S/Sds/20191029085120171796_R158_00000.jpg' })
		// this.metadatas.push({ filepath })
		// this.metadatas.push({ filepath: 'static/repos/S/Sds/20191029085120171796_R158_00000.jpg' })
		// this.metadatas.push({ filepath })
		// console.log(JSON.stringify(this.metadatas))
		// // Math.floor(Math.random()*2)
		// const fps = [
		// 	'static/repos/H/Hs/20191029085119526723_cg_00022.jpg', 
		// 	'static/repos/S/Sds/20191029085120171796_R158_00000.jpg'
		// ]

		// for (let i = 0; i < 9; i++) {
		// 	console.log(x)
		// }
	},
	methods: {
		getItem(r, c) {
			return this.metadatas[r * this.grids.cols + c];
		},
		handleSuccess(res = {}, file, fileList) {
			this.metadatas.push(res);
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
