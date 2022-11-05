$(async () => {
  axios.defaults.baseURL = JSON.parse($("#WSP_API_URL").text());

  const form = $("#formQR");
  form.addClass("d-none");
  const formName = $("#id_name")
  const formExternalUuid = $("#id_external_uuid")

  const qrCode = $("#qrCode");
  const loadingQrText = $("#loadingQRText");
  const qrLoadedText = $("#qrLoadedText");
  const sessionStarted = $("#sessionStarted");
  
  var setIntervalAsync = SetIntervalAsync.setIntervalAsync;
  var clearIntervalAsync = SetIntervalAsync.clearIntervalAsync;

  const generateBarCode = (qr) => {
      var url = 'https://api.qrserver.com/v1/create-qr-code/?data=' + encodeURIComponent(qr) + '&amp;size=50x50';
      qrCode.attr('alt', qr);
      qrCode.attr('src', url);
      qrCode.removeClass("d-none");
      loadingQrText.addClass("d-none");
      qrLoadedText.removeClass("d-none");
  }

  var context = {externalUuid: "", runs: 0}
  const timer = setIntervalAsync(async () => {
    var status = await axios.post("/qr-status", {clientId: context.externalUuid})
      .then((response) => response.data.status);

    if (status === "timedout") {
      var externalUuid = await axios.get("/qr-new")
          .then((response) => response.data.clientId);
      context.externalUuid = externalUuid;
    }
    if (status === "connected" && context.runs === 0) {
      $("#connectedH1").toggleClass("d-none");
      loadingQrText.addClass("d-none");
      await clearIntervalAsync(timer);
    } 
    
    if (status === "connected" && context.runs > 0) {
      qrCode.addClass("d-none");
      qrLoadedText.addClass("d-none");
      form.removeClass("d-none");
      await clearIntervalAsync(timer);
    }

    if (status === "not_connected") {
      var data = await axios.post("/qr-code", {clientId: context.externalUuid})
        .then((response) => response.data);
      var qr = data.qr;
      if (qrCode.attr("alt") !== qr) {
        generateBarCode(qr);
        formExternalUuid.val(context.externalUuid);
      };
    }
    context.runs++;
  }, 5000);
});
