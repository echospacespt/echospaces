from app.core.supabase import supabase


class UserRepository:

    @staticmethod
    def get_by_email(email: str):
        response = (
            supabase
            .table("users")
            .select("*")
            .eq("email", email)
            .execute()
        )

        return response.data