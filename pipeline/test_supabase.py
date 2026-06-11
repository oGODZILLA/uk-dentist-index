from supabase import create_client

SUPABASE_URL = "https://supabase.com/dashboard/project/jbafdmwjnyybbaxndbke/settings/api-keys"
SUPABASE_KEY = "sb_publishable_Ji1xxV-A8M9CFQHKffEpMw_Ef9uoDxI"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("Connected successfully!")
