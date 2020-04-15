# googlePhotoOrganizer
A python desktop app to mimic the folder structure on hard-drive with google photo's albums.

Beause google photo doesn't allow nested albums (albums inside an album), we will flatten out the folder structure, 
and preserve the folder structure information with album name.
Ex:
  On hard drive, there are 2 foldes "album1" and "album2" inside folder "album", we will create 2 album with names: 
  "album_album1" and "album_album2". If there are photos in folder "album" then there will be anothe album with the same name.
