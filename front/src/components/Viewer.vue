<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-4">
          <img
            src="@/../dist/img_res/img_in.jpg"
            alt="生成画像"
            class="img-fluid"
          />
        </div>
        <div class="col-4">
          <img
            src="@/../dist/img_res/img_style.jpg"
            alt="生成画像"
            class="img-fluid"
          />
        </div>
        <div class="col-4">
          <img
            src="@/../dist/img_res/img_out.jpg"
            alt="生成画像"
            class="img-fluid"
          />
        </div>
      </div>
    </div>
  </div>
</template>



<script>
export default {
  name: "Viewer",
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
};
</script>
