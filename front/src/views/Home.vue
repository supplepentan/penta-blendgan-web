<template>
  <div class="container">
    <div v-show="seen0">
      <Viewer />
    </div>
    <div v-show="seen1">
      <p><input type="file" v-on:change="fileSelected" /></p>
    </div>
    <div v-show="seen2">
      <button v-on:click="fileUpload">画像をアップロード</button>
    </div>
    <div v-show="seen3"><p>画像変換中</p></div>
  </div>
</template>



<script>
import axios from "axios";
import Viewer from "@/components/Viewer.vue";

export default {
  components: { Viewer },
  name: "Home",
  data: function () {
    return {
      fileInfo: "",
      // ダウンロード URL (Blob)
      downloadUrl: null,
      // ファイル名
      fileName: "",
      requestBody: "",
      seen0: false,
      seen1: true,
      seen2: false,
      seen3: false,
    };
  },
  methods: {
    fileSelected(event) {
      this.fileInfo = event.target.files[0];
      console.log("kokokokoo");
      console.log(this.fileInfo);
      this.seen2 = true;
    },
    async fileUpload() {
      const formData = new FormData();
      formData.append("file", this.fileInfo);
      console.log(this.fileInfo);
      this.seen0 = false;
      this.seen1 = false;
      this.seen2 = false;
      this.seen3 = true;
      axios.post("http://127.0.0.1:8000/upload", formData).then((response) => {
        this.seen0 = true;
        this.seen1 = true;
        this.seen3 = false;
        if (response.data.file_path) this.showUserImage = true;
      });
    },
  },
};
</script>
