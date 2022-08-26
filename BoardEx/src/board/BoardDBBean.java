package board;



import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;
import org.springframework.stereotype.Controller;

import mybatis.SqlMapClient;


public class BoardDBBean implements BoardDao {
	

   public int getCount() {
	   
       return SqlMapClient.getSession().selectOne("Board.getCount");  
    }
  
	
 
   public int insertArticle(BoardDataBean dto) {
	   int num = dto.getNum();
	   int ref = dto.getRef();
	   int re_step = dto.getRe_step();
	   int re_level = dto.getRe_level();
	   String sql=null;
	     if(num==0) {
	            // 제목글
	            
	            int count = getCount();
	            if(count !=0 ) {
	               int maxnum= SqlMapClient.getSession().selectOne("Board.maxNum");
	               ref= maxnum+1; //그룹화 아이디=글번호 최대값+1
	        
	            }
	            re_step=0;
	            re_level=0;

         		}else {
		            	//답변글
		        
		        	SqlMapClient.getSession().update("Board.updateReply", dto );
		        	re_step ++;
		            re_level ++;
		         }
	     dto.setRef(ref);
	     dto.setRe_step(re_step);
	     dto.setRe_level(re_level);
        
         return  SqlMapClient.getSession().insert("Board.insertArticle", dto );
         
       
         
      
  
   }
   
	/*
   RowMapper<BoardDataBean> rowMapper = new RowMapper<BoardDataBean>() {
	   public BoardDataBean mapRow(ResultSet rs , int count ) throws SQLException {
		   BoardDataBean dto=new BoardDataBean();
           dto.setNum(rs.getInt("num"));
           dto.setWriter(rs.getString("writer"));
           dto.setEmail(rs.getString("email"));
           dto.setSubject(rs.getString("subject"));
           dto.setPasswd(rs.getString("passwd"));
           dto.setReg_date(rs.getTimestamp("reg_date"));
           dto.setReadcount(rs.getInt("readcount"));
           dto.setRef(rs.getInt("ref"));
           dto.setRe_step(rs.getInt("re_step"));
           dto.setRe_level(rs.getInt("re_level"));
           dto.setContent(rs.getString("content"));
           dto.setIp(rs.getString("ip"));
           return dto;   
	   }
   };
   */
	
   public List<BoardDataBean> getArticles(Map<String,Integer> map){
     
        
	      
	      
             
         return SqlMapClient.getSession().selectList("Board.getArticles",map);    
      }
      
    
     
   
   
 
	
   public BoardDataBean getArticle(int num) {
       return SqlMapClient.getSession().selectOne("Board.getArticle",num);
       
   }

   public void addCount(int num) {
	 SqlMapClient.getSession().update("Board.addCount",num);	
   }
  

   public int check(int num, String passwd) {
	   		BoardDataBean dto = getArticle(num);
			int result=0;
	  		if(dto.getPasswd().equals(passwd)) {
				result = 1; //비밀번호가 다르면
			}else {
				result = 0; // 비밀번호가 같으면
			}
			return result;
	}  

	 
	  
   
   

   public int deleteArticle(int num) {
	   
		//					ref		re_step		re_level
		//제목글				10		0			0
		//ㄴ나중에 쓴 답글			10		1			1
		//ㄴ답글				10		2			1
		// ㄴ재답글			10		3			2
		
		// ref 같다		re_step + 1 같다		re_level 크다.
		
		// 답글이 있는경우	삭제된 글 입니다.
		// 답글이 없는경우	삭제
		
		BoardDataBean dto = getArticle(num); // ref, re_step, re_level 값을 가져오지 못하고 num값을 가져오기 때문에 getArticle을 가져옴
			
		
			int count = SqlMapClient.getSession().selectOne("Board.checkReply",dto);
			if(count!=0) {
				// 답글이 있는경우
				return SqlMapClient.getSession().update("Board.delArticle",num);
				
			}else {
				// 답글이 없는경우
				
				SqlMapClient.getSession().update("Board.deleteReply",dto);
				return SqlMapClient.getSession().delete("Board.deleteArticle",num);
		}
   }
		
	

	  public int modifyArticle(BoardDataBean dto) {
		   return SqlMapClient.getSession().update("Board.modifyArticle" ,dto);
	   }
		
}

// class

