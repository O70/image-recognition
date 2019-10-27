new Vue({
	el: '#app-container',
	data: function() {
		const cols = 6;
		return {
			categorys: ['W', 'WP', 'P', 'S', 'rubbled'],
			uploadVisible: false,
			disableUpload: true,
			loading: false,
			formData: null,
			metadatas: [],
			grids: {
				rows: 0, 
				cols,
				span: 24 /cols
			}
		}
	},
	computed: {
		disableSave() {
			return this.metadatas.length === 0
		}
	},
	watch: {
		metadatas() {
			this.grids.rows = Math.ceil(this.metadatas.length / this.grids.cols);
		}
	},
	created() {
		axios.get('/list').then(({ data = [] }) => {
			this.metadatas = [...data, ...this.metadatas];
		}).catch(res => {
			console.error('got error: ' + res);
		});
	},
	methods: {
		getItem(r, c) {
			return this.metadatas[r * this.grids.cols + c];
		},
		openBrowse() {
            window.open('/browse', '_blank');
		},
		appendFile(file) {
			this.formData.append('file', file.file);
		},
		handleChange(file, filelist) {
			this.disableUpload = filelist.length === 0
		},
		handleRemove(file, filelist) {
			this.disableUpload = filelist.length === 0
		},
		submitFile() {
			this.loading = true;

			this.formData = new FormData();
			this.$refs.upload.submit();

			axios.post('/upload', this.formData, {
				headers: { 'Content-Type': 'multipart/form-data' }
			}).then(({ data = [] }) => {
				this.metadatas = [...data, ...this.metadatas];
				this.$refs.upload.clearFiles();
				this.disableUpload = true;
				this.uploadVisible = false;
				this.loading = false;
			}).catch(res => {
				console.error('upload error: ' + res);
				this.loading = false;
			});
		},
		saveData() {
			this.loading = true;
			axios.post('/save', { data: JSON.stringify(this.metadatas) }).then(res => {
				console.info(res)
				this.loading = false;
			}).catch(res => {
				console.error('save error: ' + res);
				this.loading = false;
			});
		}
	}
});
