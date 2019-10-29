new Vue({
	el: '#app-container',
	data: function() {
		const cols = 3;
		return {
			metadatas: [],
			grids: {
				rows: 0, 
				cols,
				span: 24 /cols
			}
		}
	},
	watch: {
		metadatas() {
			this.grids.rows = Math.ceil(this.metadatas.length / this.grids.cols);
		}
	},
	created() {
		axios.get('/list').then(({ data = [] }) => {
			this.metadatas = data;
		}).catch(res => {
			console.error('got error: ' + res);
		});
	},
	methods: {
		getItem(r, c) {
			return this.metadatas[r * this.grids.cols + c];
		}
	}
});
