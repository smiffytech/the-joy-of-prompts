# Mounting Specific Host Folders in WSL with UNIX Permissions

When running **WSL2 with Ubuntu (or another Linux distro)**, Windows drives are mounted through the `drvfs` subsystem. By default, these mounts do not support native Linux ownership or permissions. To enable standard `chmod`, `chown`, and `umask` behavior, you must:

1. Configure `/etc/wsl.conf` to include `metadata` in automount options.
2. Use **systemd mount units** to bind specific host folders into Linux paths.

---

## /etc/wsl.conf Example

Place this file at `/etc/wsl.conf` to ensure all Windows drives are mounted with metadata and proper ownership.

```ini
[boot]
systemd=true

[automount]
options=metadata,uid=1000,gid=1000,umask=022

[interop]
appendWindowsPath=false
```

This ensures:
- **systemd** is enabled, so `.mount` units are supported.
- **metadata** emulates Linux permissions on Windows filesystems.
- **uid/gid** assign ownership to your Linux user.
- **umask=022** provides standard default permissions.
- **appendWindowsPath=false** silences noisy path translation errors.

---

## Why not use `/etc/fstab`?

Although `/etc/fstab` works on traditional Linux systems, in WSL it has two drawbacks:

- **Timing issue**: WSL’s init layer often runs `mount -a` before Windows drives are fully available. This leads to errors like:
  ```
  wsl: Processing /etc/fstab with mount -a failed
  ```
- **Duplicate handling**: With `systemd=true`, entries are also parsed by `systemd-fstab-generator`. This means mounts are attempted twice, sometimes noisily failing the first time.

👉 For reliability, use **systemd `.mount` units** instead of `/etc/fstab`.

---

## Example: Binding a Host Folder with Spaces in its Path

Suppose you want to bind:

- Host path: `C:\Users\Acer\Proton Drive\smiffytech\My files`
- Mount point in Linux: `/home/smiffy/ProtonDrive`

### Unit file name

Systemd requires the unit filename to correspond to the mount point. For `/home/smiffy/ProtonDrive`, the file must be named:

```
/etc/systemd/system/home-smiffy-ProtonDrive.mount
```

### Unit file contents

```ini
[Unit]
Description=Bind mount for ProtonDrive
After=mnt-c.mount

[Mount]
# Important:
# - In /etc/fstab, spaces must be escaped as \040
# - In systemd .mount units, use literal spaces
What=/mnt/c/Users/Acer/Proton Drive/smiffytech/My files
Where=/home/smiffy/ProtonDrive
Type=none
Options=bind

[Install]
WantedBy=multi-user.target
```

### Enable and start

```bash
sudo systemctl daemon-reload
sudo systemctl enable home-smiffy-ProtonDrive.mount
sudo systemctl start home-smiffy-ProtonDrive.mount
```

---

## Verifying

After a `wsl --shutdown` and restart, check:

```bash
mount | grep ProtonDrive
ls -ld /home/smiffy/ProtonDrive
```

You should see the Windows folder mounted, and `chmod` should now work as expected.

---

## Summary

- Configure `/etc/wsl.conf` with `metadata` to unlock UNIX-style permissions.
- Avoid `/etc/fstab` for bind mounts in WSL — use systemd mount units instead.
- When writing `.mount` files:
  - Use **literal spaces** in `What=`.
  - Match the unit filename to the target mount point path.
