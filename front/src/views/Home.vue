<template>
  <div class="markermaker">
    <div v-show="seen0">
    <p><input type="file" v-on:change="fileSelected" /></p>
    </div>
    <div v-show="seen1">
      <button v-on:click="fileUpload">画像をアップロード</button>
    </div>
    <div v-show="seen2"><p>画像変換中</p></div>
    <br />
  </div>
</template>



<script>
import axios from "axios";

export default {
  name: "markermaker",
  data: function () {
    return {
      fileInfo: "",
      // ダウンロード URL (Blob)
      downloadUrl: null,
      // ファイル名
      fileName: "",
      requestBody: "",
      seen0: true,
      seen1: false,
      seen2: false,
      seen3: false,
    };
  },
  methods: {
    fileSelected(event) {
      this.fileInfo = event.target.files[0];
      console.log("kokokokoo");
      console.log(this.fileInfo);
      this.seen1 = true;
    },
    async fileUpload() {
      const formData = new FormData();
      formData.append("file", this.fileInfo);
      console.log(this.fileInfo);
      this.seen0 = false;
      this.seen1 = false;
      this.seen2 = true;
      axios.post("http://127.0.0.1:8000/upload", formData).then((response) => {
        this.seen2 = false;
        this.seen3 = true;
        if (response.data.file_path) this.showUserImage = true;
      });
    },
  },
};
</script>
