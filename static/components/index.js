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
			labels: []
		};
	},
	watch: {
		metadatas() {
			this.grids.rows = Math.ceil(this.metadatas.length / this.grids.cols);
		}
	},
	created() {
		axios.get('/labels').then(({ data = [] }) => {
			this.labels = data;
		}).catch(res => {
			console.error('got labels error: ', res);
		});
	},
	methods: {
		getItem(r, c) {
			return this.metadatas[r * this.grids.cols + c];
		},
		findLabel(val) {
			let res = '';
			this.labels.forEach(it => {
				const label = it.children.find(sit => sit.value === val);
				label && (res = it.label + '/' + label.label);
			});

			return res;
		},
		handleSuccess(res = {}, file, fileList) {
			this.metadatas.splice(0, 0, res);
			const ind = fileList.findIndex(it => it.uid === file.uid);
			ind > -1 && fileList.splice(ind, 1);
		},
		handleChange(category, id) {
			axios.post('/update', { id, category }).then(res => {
				console.log('update category', res);
			}).catch(res => {
				console.error('update category error: ', res);
			});
		}
	}
});
