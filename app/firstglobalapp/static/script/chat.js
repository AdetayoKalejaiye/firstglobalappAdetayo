$(document).ready(function() {
    // Handle button click event
    $(".initiate-chat-btn").click(function() {
        var receiverId = $(this).data("receiver-id");
        window.location.href = "/chat/user_chat/" + receiverId + "/";
    });
});