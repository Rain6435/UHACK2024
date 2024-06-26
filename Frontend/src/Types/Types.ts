export type ReportObjectProps = {
  id: number;
  location_id: number;
  team_id: number;
  is_dangerous: boolean;
  creation_date: string;
  lead_time: string;
  fix_date: string;
  status: string;
  initialStatus:string;
  image: string;
  requestor_id: number;
  adresse:string;
};

export type TeamInfo = {
  id: number;
  name: string;
  password: string;
  work_time: string;
  work_season: string;
  secteur: string;
  is_admin: boolean;
};
