new Vue({
	el: '#app-container',
	data() {
		return {
			metadatas: [],
			historys: [],
			categorys: [],
			labels: [],
			drawer: false,
			selected: '0'
		};
	},
	watch: {
		selected() {
			(this.selected === '0') && this.getList();
		}
	},
	created() {
		axios.get('/labels').then(({ data = [] }) => {
			this.labels = data;
		}).catch(res => {
			console.error('got labels error: ', res);
		});

		this.getList();
	},
	methods: {
		getList() {
			axios.get('/list').then(({ data = [] }) => {
				this.historys = data;
			}).catch(res => {
				console.error('got error: ' + res);
			});
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

			(this.selected != '3') && (this.selected = '3')
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
		},
		handleDownload() {
			this.$notify({
				title: '消息',
				message: '制作中......',
				type: 'info'
			});
		}
	}
});
