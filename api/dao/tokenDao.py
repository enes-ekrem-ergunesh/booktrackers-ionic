from dao.baseDao import BaseDAO, execute_query_single, execute_update


class TokenDAO(BaseDAO):
    def __init__(self):
        super().__init__('tokens')

    def get_by_token(self, token):
        query = f"SELECT * FROM {self.table} WHERE token = %s"
        return execute_query_single(query, (token,))

    def revoke(self, token):
        query = f"UPDATE {self.table} SET revoked_at = CURRENT_TIMESTAMP WHERE token = %s"
        execute_update(query, (token,))