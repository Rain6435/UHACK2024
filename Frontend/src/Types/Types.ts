export type ReportObjectProps = {
  id: number;
  location_id: number;
  team_id: number;
  is_dangerous: boolean;
  creation_date: Date;
  lead_time: Date;
  fix_date: Date;
  status: string;
  initialStatus:string;
  image_path: string;
  requestor_id: number;
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
