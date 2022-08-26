package mybatis;

import java.io.IOException;
import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class SqlMapClient {
	private static SqlSession session;
	static {
		String resource ="mybatis/sqlMapConfig.xml";
		
		try {
			Reader reader = Resources.getResourceAsReader(resource);
			SqlSessionFactory factory= new SqlSessionFactoryBuilder().build(reader);
			session = factory.openSession( true );
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static SqlSession getSession() {
		return session;
	}


}
