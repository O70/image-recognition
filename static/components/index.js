new Vue({
	el: '#app-container',
	data() {
		const cols = 4;
		const hcols = 2;
		return {
			metadatas: [],
			grids: {
				rows: 0, 
				cols,
				span: 24 / cols
			},
			hgrids: {
				rows: 0, 
				cols,
				span: 24 / hcols
			},
			categorys: [],
			labels: [],
			drawer: false,
			historys: []
		};
	},
	watch: {
		metadatas() {
			this.grids.rows = Math.ceil(this.metadatas.length / this.grids.cols);
		},
		historys() {
			this.hgrids.rows = Math.ceil(this.historys.length / this.hgrids.cols);
		}
	},
	created() {
		axios.get('/labels').then(({ data = [] }) => {
			this.labels = data;
		}).catch(res => {
			console.error('got labels error: ', res);
		});

		axios.get('/list').then(({ data = [] }) => {
			this.historys = data;
		}).catch(res => {
			console.error('got error: ' + res);
		});
	},
	methods: {
		getItem(r, c) {
			return this.metadatas[r * this.grids.cols + c];
		},
		getHistoryItem(r, c) {
			return this.historys[r * this.hgrids.cols + c];
		},
		findLabel(val) {
			let res = {};
			this.labels.forEach(it => {
				const lab = it.children.find(sit => sit.value === val);
				lab && (res = { label: it.label + '/' + lab.label, describe: lab.describe || 'None' });
			});

			return res;
		},
		handleSuccess(res = {}, file, fileList) {
			this.metadatas.splice(0, 0, res);
			const ind = fileList.findIndex(it => it.uid === file.uid);
			ind > -1 && fileList.splice(ind, 1);
		},
		handleChange(category, md, pred) {
			axios.post('/update', { id: md.id, category }).then(res => {
				console.log('update category', res);
				const lab = this.findLabel(category);
				Vue.set(md, 'filepath', res.data.filepath);
				Vue.set(pred, 'label', lab.label);
				Vue.set(pred, 'describe', lab.describe);
			}).catch(res => {
				console.error('update category error: ', res);
			});
		}
	}
});
