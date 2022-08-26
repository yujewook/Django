<%@page import="board.BoardDBBean"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ include file="setting.jsp"%>
<link type="text/css" rel="stylesheet" href="${project}/board/style_board.css">
<script src="${project}/board/script.js"></script>

<h2>${page_delete}</h2>

<c:if test="${result eq 0}">
		<script type="text/javascript">
			<!--
			alert(modifyerror);
			//-->
		</script>
		<meta http-equiv="refresh" content="0; url=list.do?pageNum=${pageNum}">
</c:if>
<c:if test="${result ne 0}">
	<c:redirect url="list.do?pageNum=${pageNum}"/>
</c:if>